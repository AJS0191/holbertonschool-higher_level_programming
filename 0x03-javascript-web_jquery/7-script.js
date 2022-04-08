#!/usr/bin/node
let daName;
$( "header" ).css("color", '#FF0000')
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function(data) {
    console.log(data.name)
    $( '#character' ).append('<p>' + data.name + '<p>')
  }
})
