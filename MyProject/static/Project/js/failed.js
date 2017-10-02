$(document).ready(function() {
  $('#fullpage').fullpage({
    sectionsColor: ['#616161'],
    navigation: false,
	navigationPosition: 'left',
	navigationTooltips: ['Home'],
	showActiveTooltip: true,
	controlArrows: true,
	loopHorizontal: false,
	slidesNavigation: false,
	loopTop: true,
	loopBottom: true,
	fixedElements: '#footer'
    });
});
