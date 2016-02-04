
/*************************************
Author : Satabdi Ganguly
Title : Custom Widjet
Version : 2.3
*****************************/



window.onload=function(){
    //Get Canvas related information
    var canvas=document.getElementById("canvas");
    var ctx=canvas.getContext("2d");
    var canvas1=document.getElementById("canvas1");
    var ctx1=canvas.getContext("2d");
    var BB=canvas.getBoundingClientRect();
    var offsetX=BB.left;
    var offsetY=BB.top;
    var WIDTH = canvas.width;
    var HEIGHT = canvas.height;
    var intersect=false;
    var AloeStatus;
    var PeaceStatus;
    var divele=document.getElementById("status");
    var rect={x:200,y:210,w:200,h:40};
    var rectAloe={x:650, y: 50, w:150, h:40}
    var rectPeace={x:650, y: 150, w:150, h:40}
    var sad=new Image();
    sad.src="sad.png";
    var happy=new Image();
    happy.src="happy.png";
    var inAloe=false;

    setBB();
    //Listen for mouse movements
    canvas.onmousedown = myDown;
    //canvas.onmouseup = myUp;
    canvas.onmousemove = myMove;
    var FPS = 30;
    setInterval(function(){
        draw();


    }, 1000/FPS);
    //Draw the scene




    function myDown(e)
    {
      e.preventDefault();
      e.stopPropagation();
      var mx=e.clientX-BBoffsetX;
      var my=e.clientY-BBoffsetY;
      if(mx>=rect.x && mx<=rect.x+rect.w && my>=rect.y && my<=rect.y+rect.h){

        location.href="http://localhost:63342/HappyPlant/HelloPlantDashboard.html";
      }
      if(mx>=rectAloe.x && mx<=rectAloe.x+rectAloe.w && my>=rectAloe.y && my<=rectAloe.y+rectAloe.h){

        location.href="http://192.168.1.97:8000/";
      }
      if(mx>=rectPeace.x && mx<=rectPeace.x+rectPeace.w && my>=rectPeace.y && my<=rectPeace.y+rectPeace.h){

        location.href="http://192.168.1.24:8000/";
      }
     }


     function myMove(e)
     {
          e.preventDefault();
          e.stopPropagation();
          var mx=e.clientX-BBoffsetX;
          var my=e.clientY-BBoffsetY;
          if(mx>=rectAloe.x && mx<=rectAloe.x+rectAloe.w && my>=rectAloe.y && my<=rectAloe.y+rectAloe.h){
                inAloe=true;
                if(inAloe == true)
                {

                    ctx.fillStyle="#4C4C4C";
                    ctx.font = "12.8px arial message-box";
                    ctx.fillText("Click here to get Status for Aloe", rectAloe.x, rectAloe.y+60);
                }

            }
            else
            {
                inAloe=false;

                ctx.fillStyle="white";
                ctx.font = "12.8px sans-serif message-box";
                ctx.fillText("Click here to get Status for Aloe", rectAloe.x, rectAloe.y+60);
            }

            if(mx>=rectPeace.x && mx<=rectPeace.x+rectPeace.w && my>=rectPeace.y && my<=rectPeace.y+rectPeace.h){
                ctx.fillStyle="#4C4C4C";
                ctx.font = "12.8px arial";
                ctx.fillText("Click here to get Status for PeaceLily", rectPeace.x, rectPeace.y+60);


            }
            else
            {
                ctx.fillStyle="white";
                ctx.font = "12.8px arial";
                ctx.fillText("Click here to get Status for PeaceLily", rectPeace.x, rectPeace.y+60);


            }



     }







    function setBB(){
      BB=canvas.getBoundingClientRect();
      BBoffsetX=BB.left;
      BBoffsetY=BB.top;
      }



    function draw() {
        drawAloeButton();
        drawPeaceButton();

        getDataAloe();
        getDataPeace();

    }

    function drawAloeButton()
    {
        ctx.beginPath();
        ctx.rect(rectAloe.x,rectAloe.y,rectAloe.w,rectAloe.h);
        ctx.closePath();
        ctx.fillStyle="#897cc3"
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#003300';
        ctx.stroke();
        ctx.fillStyle="black";
        ctx.font = "10pt sans-serif";

        ctx.fillText("Status of Aloe", rectAloe.x+20, rectAloe.y+20);

    }

    function drawPeaceButton()
    {
        ctx.beginPath();
        ctx.rect(rectPeace.x,rectPeace.y,rectPeace.w,rectPeace.h);
        ctx.closePath();
        ctx.fillStyle="#897cc3"
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#003300';
        ctx.stroke();
        ctx.fillStyle="black";
        ctx.font = "10pt sans-serif";

        ctx.fillText("Status of Peace Lily", rectPeace.x+10, rectPeace.y+20);

    }

     function getDataAloe()
    {
        var temp;
        var stat = false;
        jQuery.ajax({
        url: "http://192.168.1.97:8000/",
        success: function(result) {
            var html = jQuery('<p>').html(result);
            ctx.font = "15pt sans-serif";
            ctx.fillStyle="black";
            ctx.fillText("Status for Aloe Vera Plant: ", 10, 50);
            temp=html.find("p#status").html();
            temp=temp.toLowerCase();
            if(temp.indexOf("ok")>-1)
            {
               ctx.fillStyle="#9f8fe5";
               temp="Plant is okay";
               stat=false;
            }
            else
            {
                temp="Plant Needs Watering";
                ctx.fillStyle="#FF3232";
                stat=true;
            }
             ctx.font = "15pt sans-serif";
             ctx.fillText(temp , 270, 50);
             if(stat == true)
                ctx.drawImage(sad, 500, 0, height=100, width=100);
             else
                 ctx.drawImage(happy, 500, 0, height=100, width=100);

        },
    });


    }

    function getDataPeace()
    {
        var temp;
        var stat = false;
        jQuery.ajax({
        url: "http://192.168.1.24:8000/",
        success: function(result) {
            var html = jQuery('<p>').html(result);
            ctx.font = "15pt sans-serif";
            ctx.fillStyle="black";
            ctx.fillText("Status for Peace Lily Plant: ", 10, 150);

            //alert(html.find("p#status").attr("id"));
            temp=html.find("p#status").html();
            //alert(html.find("p#status"));
            //alert(AloeStatus);
            temp=temp.toLowerCase();
            if(temp.indexOf("ok")>-1)
            {
               ctx.fillStyle="#9f8fe5";
               temp="Plant is okay";
               stat=false;
            }
            else
            {
                ctx.fillStyle="#FF3232";
                temp="Plant Needs Watering";
                stat=true;
            }
             ctx.font = "15pt sans-serif";
            ctx.fillText(temp , 270, 150);
            if(stat==true)
                ctx.drawImage(sad, 500, 90, height=100, width=100);
            else
                ctx.drawImage(happy, 500, 90, height=100, width=100);

        },
    });
    }



};


