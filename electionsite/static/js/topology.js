var width = 800,
  height = 450;
var svg = d3.select('.graphics').append('svg')
  .attr('width', width)
  .attr('height', height)
  .attr('class', 'map');
var state_data = getStateData();
var projection = d3.geo.albersUsa()
  .scale(1000)
  .translate([width / 2, height / 2]);
var path = d3.geo.path()
  .projection(projection);
var ttip = d3.select("body").append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);
d3.json('static/states.json', function(error, us) {
  svg.selectAll('.states')
    .data(topojson.feature(us, us.objects.usStates).features)
    .enter()
    .append('path')
    .attr('class', function(d, e){
      return 'states ' + e; 
    })
    .attr('d', path)
    .style("fill", function(d) {
      var abbrev = d.properties.STATE_ABBR;
      if (state_data[abbrev] == undefined) return "white";
      var total = state_data[abbrev].total;
      var republican = state_data[abbrev].republican;
      var democratic = state_data[abbrev].democratic;
      if (republican / total > 0.50) {
        return "#D91F2F";
      } else {
        return "#3853A4";
      }
    })
    .on('mouseover', function(d) {
      var abbrev = d.properties.STATE_ABBR;
      var state = state_data[abbrev];
      ttip.style("display", "block").style("opacity", "1");
      ttip.html(
          "<b>" + state.name + "</b><br/>" +
          "<p class='left'><b>Total:</b> " + state.total + "</p>" +
          "<p class='left'><b>Democratic:</b> " + state.democratic + "</p>" +
          "<p class='left'><b>Republican:</b> " + state.republican + "</p>"
        )
        .style("left", (d3.event.pageX + 30) + "px")
        .style("top", (d3.event.pageY + 30) + "px");
    })
    .on('mouseout', function(d) {
      ttip.style("display", "none").style("opacity", "0");;
    })
    .on('click', function(d, e) {
      var abbrev = d.properties.STATE_ABBR;
      $('.states').removeClass("active");
      $('.'+e).addClass("active");
      if (abbrev !== undefined) {
        showGraph(abbrev);
        showTweetsForState(abbrev);
      }
    });
});


function showGraph(abbrev) {
  var responsiveWidth = $(window).width()/2;
  var margin = {
      top: 40,
      right: 100,
      bottom: 100,
      left: 40
    },
    width = responsiveWidth - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .range([0, width]);

    var y = d3.scale.ordinal()
        .rangeRoundBands([0, height], 0.1);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .tickSize(0)
        .tickPadding(3);

  $('.chart > svg').remove();

  var chart = d3.select(".chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var data = state_data[abbrev].details;
  x.domain([d3.min(data, function(d){ return parseFloat(d.sentiment_total) }), d3.max(data, function(d){ return Math.max(0, parseFloat(d.sentiment_total)); })]);
  y.domain(data.map(function(d) { return d.candidate; }));

  chart.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("fill", function(d) {
        if (d.party.toLowerCase() == "republican") return "#E23746"; //red
        else return "#5975C6"; //blue
      })
      .attr("width", 0)
      .transition()
      .duration(400)
      .attr("class", function(d) { return "bar bar--" + (d.sentiment_total < 0 ? "negative" : "positive"); })
      .attr("x", function(d) { return x(Math.min(0, d.sentiment_total)); })
      .attr("y", function(d) { return y(d.candidate); })
      .attr("width", function(d) { return Math.abs(x(d.sentiment_total) - x(0)); })
      .attr("height", y.rangeBand());

  chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  chart.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(" + x(0) + ",0)")
      .call(yAxis);

  chart.append("text")
    .attr("y", height + margin.top)
    .attr("x", width/2)
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Public Sentiment");
    
  chart.append("text")
    .attr("x", (width / 2))
    .attr("y", 0 - (margin.top / 3))
    .attr("text-anchor", "middle")
    .style("font-size", "25px")
    .text(state_data[abbrev].name + " Projections");
}

function type(d) {
  d.sentiment_total = +d.sentiment_total;
  return d;
}

function showTweetsForState(abbrev){
  if (abbrev == "") return;
  $.ajax({
    url: "/states/"+abbrev,
    type: 'GET',
    success: function(results){
      $('.stateData').empty();
      $('.stateData').append('<h3>Passionate Sentiments From ' + results.state + '</h3>');
      var list = results.data.map(function(data){
          return '<div class="singleTweet"><b>' + data.author + ':</b>' + '<p style="margin-left: 15px;"> ' + data.text.replace(/((http|https|ftp):\/\/[\w?=&.\/-;#~%-]+(?![\w\s?&.\/;#~%"=-]*>))/g, '<a href="$1" target="_blank">$1</a> ') + '</p><p style="margin-left: 15px;">Sentiment Value: <b>' + data.sentiment + '</b></p></div>';
      });
      $('.stateData').append('<div>' + list.toString().split(",").join("") + '</div>');
    }
  });
}