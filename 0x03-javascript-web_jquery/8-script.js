#!/usr/bin/node
let daName;
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function(data) {
    console.log(data)
    console.log(data.results)
    console.log(data.results[0].title)
    $.each(data.results, function(i) {
      $('#list_movies').append('<li>' + data.results[i].title + '</li>')
      console.log(data.results)
    })
  }
})
