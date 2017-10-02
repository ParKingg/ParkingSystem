$(document).ready(function() {
  $('#fullpage').fullpage({
    sectionsColor: ['#404040', '#F7F7F7'],
    navigation: true,
	navigationPosition: 'left',
	navigationTooltips: ['Park', 'Map', 'About'],
	showActiveTooltip: true,
	controlArrows: true,
	loopHorizontal: false,
	slidesNavigation: true,
	loopTop: true,
	loopBottom: true
    });
});

$(document).ready(function(){
    // Hide the Modal
    $("#cancelbtn").click(function(){
        $("#myModalCancel").modal("hide");
    });
});