const menuIcon = document.getElementById("icon-menu");
const menuList = document.getElementById("navigation");

menuIcon.addEventListener("click",()=>{
  menuList.classList.toggle("hidden")
});