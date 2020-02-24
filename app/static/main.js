$(".dropdown-menu a").click(function(){
    loadContent($(this).text());
});

$(".dropdown-menu input").keyup(function(e){
    if(e.keyCode == 13)
    {
        loadContent($(this).val());
    }
});

var saveContentPeriodically = function(){
    saveContent();
    setTimeout(saveContentPeriodically, 2000);
  };
setTimeout(saveContentPeriodically, 2000);

var lastSavedContentKey;
var lastSavedContentValue;
function saveContent() {
    var contentKey = $('#contentKey').text().trim();
    var contentValue = $('#contentValue').val();
    if (lastSavedContentKey == contentKey && lastSavedContentValue == contentValue) {
        return;
    }
    lastSavedContentKey = contentKey;
    lastSavedContentValue = contentValue;
    $.ajax({
        url: '/content',
        type: 'PUT',
        data: {'contentValue' : contentValue, 'contentKey': contentKey}
      });
    console.log("update button clicked.")
};

function loadContent(item) {
    $('#contentKey').text(item);
    localStorage.setItem("contentKey", item);
    $.get( "/content?contentKey="+item, function( data ) {
        $("#contentValue").val(data);
        console.log(data)
    });    
}

var contentKey = localStorage.getItem("contentKey")
if (!contentKey) {
    contentKey = "Default"
}
loadContent(contentKey);
