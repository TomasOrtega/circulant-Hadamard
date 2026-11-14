export function bindVideoCut(video) {
  const start = Number(video.dataset.cutStart);
  const end = Number(video.dataset.cutEnd);
  if (
    !Number.isFinite(start) ||
    !Number.isFinite(end) ||
    start < 0 ||
    end <= start
  )
    return () => {};

  const initialize = () => {
    video.currentTime = start;
  };
  const constrain = () => {
    if (video.currentTime < start) video.currentTime = start;
    else if (video.currentTime >= end) {
      video.pause();
      if (video.currentTime !== end) video.currentTime = end;
    }
  };
  const replay = () => {
    if (video.currentTime < start || video.currentTime >= end)
      video.currentTime = start;
  };
  const handlers = {
    loadedmetadata: initialize,
    seeking: constrain,
    timeupdate: constrain,
    play: replay,
  };
  for (const [event, handler] of Object.entries(handlers))
    video.addEventListener(event, handler);
  if (video.readyState >= 1) initialize();
  return () => {
    for (const [event, handler] of Object.entries(handlers))
      video.removeEventListener(event, handler);
  };
}

if (typeof document !== "undefined") {
  document.querySelectorAll("video[data-cut-start]").forEach(bindVideoCut);
}
