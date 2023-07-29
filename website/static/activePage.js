const currentLocation = location.href;
const menuItem = document.querySelectorAll('a');
const menuLength = menuItem.length
for (let i = 0; i<menuLength; i++){
    if (currentLocation.includes(menuItem[i].href) && currentLocation != menuItem[0].href){
        menuItem[0].classList.remove("active")
        menuItem[i].className = "active"
    }
    else if (currentLocation === menuItem[0].href) {menuItem[0].className = "active"}
}