const toggler = document.querySelector("#toggleTheme");
const element = document.documentElement;

toggler.addEventListener("mouseup", () => {
  if (element.classList.contains("dark")) {
    element.classList.remove("dark");
    localStorage.setItem("theme", "light");
  } else {
    element.classList.add("dark");
    localStorage.setItem("theme", "dark");
  }
});
