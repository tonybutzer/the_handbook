<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">

    <style type="text/css">
      body {font-size: 1.6em;}
      .hidden {display:none;}
      .show {display:inline !important;}
      button {
        border: 2px solid black; background: #E5E4E2;
        font-size: .5em; font-weight: bold; color: black;
        padding: .8em 2em;
        margin-top: .4em;
      }
    </style>

  </head>
  <body>
  <p id="sayHello"></p>
  <script>
   // You create variables that store values with var
  // Prompt opens a popup that requests info
  var yourName = prompt("What is your name?");

  // If performs different actions depending on conditions
  if(yourName != null){

    // Set text in an HTML element with the id sayHello
    // You concatenate (combine) strings with +
    document.getElementById("sayHello").innerHTML = "Hello " + yourName;
  } else {

    // Alert opens a popup that contains a message
    alert("Please Enter Your Name Next Time");
  }

  </script>
  </body>
