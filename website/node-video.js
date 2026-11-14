export function validateVideo(video, title) {
  if (video == null) return;
  if (Boolean(video.youtubeId) === Boolean(video.src)) {
    throw new Error(`Choose one video source for ${title}`);
  }
  if (video.youtubeId && !/^[A-Za-z0-9_-]{11}$/.test(video.youtubeId)) {
    throw new Error(`Invalid YouTube ID for ${title}`);
  }
  if (
    video.duration != null &&
    (!Number.isFinite(video.duration) || video.duration <= 0)
  ) {
    throw new Error(`Invalid video duration for ${title}`);
  }
}

export function validateSegment(segment, video, title) {
  if (segment == null) return;
  const { start, end } = segment;
  if (
    !Number.isFinite(start) ||
    !Number.isFinite(end) ||
    start < 0 ||
    end <= start
  ) {
    throw new Error(`Invalid cut range for ${title}`);
  }
  if (video?.duration != null && end > video.duration) {
    throw new Error(`Cut exceeds overview duration for ${title}`);
  }
  if (
    video?.youtubeId &&
    (!Number.isInteger(start) || !Number.isInteger(end))
  ) {
    throw new Error(`YouTube cut times must be whole seconds for ${title}`);
  }
}

export const cutVideo = (node, child) =>
  node.video && child.segment
    ? { ...node.video, segment: child.segment }
    : null;

export const mediaUrl = (source, base) =>
  /^https?:\/\//.test(source) ? source : `${base}${source}`;

export function formatTime(seconds) {
  const whole = Math.floor(seconds);
  const hours = Math.floor(whole / 3600);
  const minutes = Math.floor((whole % 3600) / 60);
  const remainder = String(whole % 60).padStart(2, "0");
  return hours
    ? `${hours}:${String(minutes).padStart(2, "0")}:${remainder}`
    : `${minutes}:${remainder}`;
}
