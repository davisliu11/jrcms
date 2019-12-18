$(".dropdown-menu a").click(function(){
    loadContent($(this).text());
});

$(".dropdown-menu input").keyup(function(e){
    if(e.keyCode == 13)
    {
        loadContent($(this).val());
    }
});

$("#contentValue").keyup(function(e){
    saveContent()
});

function saveContent() {
    $.ajax({
        url: '/content',
        type: 'PUT',
        data: {'contentValue' : $('#contentValue').val(), 'contentKey': $('#contentKey').text().trim()}
      });
}

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
