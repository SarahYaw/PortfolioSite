// code inspo from https://www.w3schools.com/howto/howto_js_slideshow.asp
var slideIndex = [1, 1];
let slideSetList = ["code-projects", "art-projects"]

showSlides(1, 0);
showSlides(1, 1);

function plusSlides(increment, slideSetId) {
    // number in position slideSetId of slideSetList plus increment is new slide num
    newSlideNum = slideIndex[slideSetId] + increment
    showSlides(newSlideNum, slideSetId);
}

function showSlides(newId, codeOrArt) {
    let parent = document.getElementById(slideSetList[codeOrArt])
    let slideSet = parent.querySelectorAll(".slide")
    
    if (newId >= slideSet.length) {
        newId = 0
    }    
    if (newId < 0) {
        newId = slideSet.length-1
    }
    for (let i = 0; i < slideSet.length; i++) {
        slideSet[i].style.display = "none";  
    }
    slideIndex[codeOrArt] = newId
    slideSet[slideIndex[codeOrArt]].style.display = "flex";
}