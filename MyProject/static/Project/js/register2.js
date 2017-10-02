$(document).ready(function() {
  $('#fullpage').fullpage({
  sectionsColor: ['#F7F7F7'],
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

$(document).ready(function(){
    $('[data-toggle="popover"]').popover();   
});