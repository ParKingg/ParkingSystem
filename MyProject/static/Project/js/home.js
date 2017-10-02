$(document).ready(function() {
  $('#fullpage').fullpage({
    sectionsColor: ['#F7F7F7','#F7F7F7','#F7F7F7','#F7F7F7'],
    navigation: false,
	navigationPosition: 'left',
	showActiveTooltip: true,
	controlArrows: true,
	loopHorizontal: false,
	slidesNavigation: true,
	loopTop: true,
	loopBottom: true,
	fixedElements: '#footer',
	anchors: ['home', 'howitworks', 'contactus', 'aboutus', 'footer'],
	menu: '#menu',
	keyboardScrolling: true,
	paddingBottom: 0
    });
});
