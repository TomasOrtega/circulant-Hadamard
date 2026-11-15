const controls = document.getElementById("page-controls");
const topButton = document.getElementById("jump-to-top");
const darkButton = document.getElementById("dark-mode-toggle");
const root = document.documentElement;
const setDarkMode = (dark) => {
  root.classList.toggle("dark", dark);
  darkButton.setAttribute("aria-checked", String(dark));
};
setDarkMode(root.classList.contains("dark"));
darkButton.hidden = false;
darkButton.addEventListener("click", () => {
  const dark = !root.classList.contains("dark");
  setDarkMode(dark);
  try {
    localStorage.setItem("dark-mode", String(dark));
  } catch {}
});
window.addEventListener("storage", (event) => {
  if (event.key === "dark-mode") setDarkMode(event.newValue === "true");
});
window.addEventListener("beforeprint", () => root.classList.remove("dark"));
window.addEventListener("afterprint", () => setDarkMode(darkButton.getAttribute("aria-checked") === "true"));

const toc = document.getElementById("table-of-contents");
const tocButton = document.getElementById("toc-toggle");
const tocClose = document.getElementById("toc-close");
const masthead = document.querySelector("body > header");
const desktop = window.matchMedia("(min-width: 70rem)");
const headings = [...document.querySelectorAll("main h1, main h2, main h3")];
if (headings.length > 1) {
  document.getElementById("toc-links").replaceChildren(...headings.map((heading, index) => {
    const section = heading.parentElement.matches("header") ? heading.parentElement.parentElement : null;
    const target = heading.id || section?.id || (heading.id = `toc-heading-${index}`);
    const link = document.createElement("a");
    link.href = `#${target}`;
    link.className = "block p-2 text-black no-underline hocus:bg-light-gray hocus:text-theme";
    link.style.paddingLeft = `${Number(heading.tagName[1]) * 0.5}rem`;
    link.innerHTML = heading.innerHTML;
    link.querySelectorAll("hr").forEach(rule => rule.remove());
    link.querySelectorAll("[id]").forEach(label => label.removeAttribute("id"));
    if (index === 0) link.addEventListener("click", () => setTocOpen(false));
    return link;
  }));
}
const updateScrollControls = () => {
  topButton.hidden = window.scrollY <= 500;
  tocButton.inert = headings.length < 2 || !toc.inert || headings[0].getBoundingClientRect().bottom > 0;
};
window.addEventListener("scroll", updateScrollControls, { passive: true });
window.addEventListener("resize", updateScrollControls);
updateScrollControls();

const setTocOpen = (open, focus = false) => {
  toc.inert = !open;
  tocButton.setAttribute("aria-expanded", String(open));
  root.classList.toggle("toc-open", open);
  updateScrollControls();
  if (focus) (open ? tocClose : tocButton.inert ? masthead.querySelector("a") : tocButton).focus();
};
tocButton.addEventListener("click", () => setTocOpen(true, true));
tocClose.addEventListener("click", () => setTocOpen(false, true));
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !toc.inert) {
    setTocOpen(false, true);
    event.preventDefault();
  }
});
document.addEventListener("pointerdown", (event) => {
  if (!desktop.matches && !toc.inert && !toc.contains(event.target) && !tocButton.contains(event.target))
    setTocOpen(false);
});

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
