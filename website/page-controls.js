const controls = document.getElementById("page-controls");
const topButton = document.getElementById("jump-to-top");

const updateTopButton = () => {
  topButton.hidden = window.scrollY <= 500;
};
window.addEventListener("scroll", updateTopButton, { passive: true });
updateTopButton();

topButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
      ? "instant"
      : "smooth",
  });
});

document.getElementById("share-page").addEventListener("click", async () => {
  const url = window.location.href;
  if (navigator.share) {
    try {
      await navigator.share({ title: document.title, text: document.title, url });
      return;
    } catch (error) {
      if (error.name === "AbortError") return;
    }
  }
  try {
    await navigator.clipboard.writeText(url);
    window.alert("Link copied to clipboard!");
  } catch {
    window.prompt("Copy this page's link:", url);
  }
});

controls.hidden = false;
