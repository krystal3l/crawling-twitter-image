if(getCookie("notToday")!="Y"){
    $("#myModal").show();
}

function closePopupNotToday(){
    setCookie('notToday','Y', 1);
    $("#myModal").hide('fade');
}

function setCookie(name, value, expiredays) {
    var today = new Date();
    today.setDate(today.getDate() + expiredays);
    document.cookie = name + '=' + escape(value) + '; path=/; expires=' + today.toGMTString() + ';'
}

function getCookie(name)
{
    var cName = name + "=";
    var x = 0;
    while ( x <= document.cookie.length )
    {
        var y = (x+cName.length);
        if ( document.cookie.substring( x, y ) == cName )
        {
            if ( (endOfCookie=document.cookie.indexOf( ";", y )) == -1 )
                endOfCookie = document.cookie.length;
            return unescape( document.cookie.substring( y, endOfCookie ) );
        }
        x = document.cookie.indexOf( " ", x ) + 1;
        if ( x == 0 )
            break;
    }
    return "";
}

function closeMainPopup(){
    $("#myModal").hide('fade');
}

$(function(){
    $('#btn').click(function(){
        var q1_submit = $("#q1").val();
        var q2_submit = $("#q2").val();

        if ((q1_submit == "") || (q2_submit == ""))
        {
            alert("정답을 입력해주세요");
            return;
        } else {
            if ((q1_submit == "심재영") && (q2_submit == "01-23"))
            {
                alert("정답입니다!");
                closePopupNotToday();
            } else {
                alert("틀렸습니다.");
                return;
                }
            }
    });
});
