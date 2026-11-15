import { describe, expect, test } from "bun:test";
import { bindVideoCut } from "../video-player.js";

class Video extends EventTarget {
  dataset = { cutStart: "10", cutEnd: "30" };
  currentTime = 0;
  readyState = 0;
  paused = true;
  pause() {
    this.paused = true;
  }
  play() {
    this.paused = false;
    this.dispatchEvent(new Event("play"));
  }
  emit(event) {
    this.dispatchEvent(new Event(event));
  }
}

describe("native video cut playback", () => {
  test("metadata seeks to the start and playback stops at the end", () => {
    const video = new Video();
    bindVideoCut(video);
    video.emit("loadedmetadata");
    expect(video.currentTime).toBe(10);
    video.play();
    video.currentTime = 31;
    video.emit("timeupdate");
    expect(video.paused).toBe(true);
    expect(video.currentTime).toBe(30);
  });

  test("replay starts the cut again, and seeking cannot escape its range", () => {
    const video = new Video();
    video.readyState = 1;
    bindVideoCut(video);
    expect(video.currentTime).toBe(10);
    video.currentTime = 30;
    video.play();
    expect(video.currentTime).toBe(10);
    expect(video.paused).toBe(false);
    video.currentTime = 0;
    video.emit("seeking");
    expect(video.currentTime).toBe(10);
    video.currentTime = 90;
    video.emit("seeking");
    expect(video.currentTime).toBe(30);
    expect(video.paused).toBe(true);
  });

  test("invalid ranges are ignored and listeners can be removed", () => {
    const invalid = new Video();
    invalid.dataset.cutEnd = "5";
    bindVideoCut(invalid);
    invalid.emit("loadedmetadata");
    expect(invalid.currentTime).toBe(0);
    const video = new Video();
    const cleanup = bindVideoCut(video);
    cleanup();
    video.emit("loadedmetadata");
    expect(video.currentTime).toBe(0);
  });
});
