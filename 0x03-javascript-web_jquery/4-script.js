#!/usr/bin/node
$( '#toggle_header' ).click(function() {
  $( "header" ).toggleClass("green");
  $( "header" ).toggleClass("red");
})
