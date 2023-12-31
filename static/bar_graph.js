async function graph() {
    const data = await d3.json("/static/reviews.json");
    data.forEach((item) => {
      item.rating = +item.rating;
    });
    const margin = {
      top: 100,
      bottom: 100,
      left: 50,
      right: 50,
    };

    var graph_h = 900 - margin.top - margin.bottom;
    var graph_w = 900 - margin.left - margin.right;

    const innerHeight = 300 - margin.top - margin.bottom;
    const innerWidth =
      (innerHeight + margin.top + margin.bottom) * 2 -
      margin.left -
      margin.right;

    build_graph();

    function build_graph() {
      // select div and create an svg container
      const svg = d3
        .select("#container")
        .append("svg")
        .attr("height", graph_h)
        .attr("width", graph_w)
        .style("background-color", "white");

      // create tooltip for bar graph
      const tooltip = d3
        .select("#container")
        .append("div")
        .attr("class", "tip")
        .style("position", "absolute")
        .style("visibility", "visibility");

      // append group element to the svg window will be used as an svg container
      const g = svg
        .append("g")
        .attr(
          "transform",
          `translate(${margin.left + 10}, ${margin.top - 80})`
        );

      // create scales for X-axis
      const Xscale = d3
        .scaleBand()
        .paddingInner(0.2)
        .paddingOuter(0.4)
        .domain(
          data.map((d, i) => {
            return d.genera;
          })
        )
        .range([0, graph_w - 300]);

      // create scales for Y-axis
      const Yscale = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(data, (d) => {
            return d.rating + 2;
          }),
        ])
        .range([graph_h - 300, 0]);

      // create rectangles for bar graph and add
      const rects = g
        .selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", (d, i) => Xscale(d.genera) + 20.0)
        .attr("y", graph_h - 300)
        .attr("height", 0)

        .attr("width", Xscale.bandwidth() - 50)
        .attr("fill", "steelblue")
        .on("mouseover", (d, i) => {
          return tooltip
            .html("vote count: " + i.votes + " <br>rating: " + i.rating)
            .style("visibility", "visible")
            .style("top", Yscale(i.rating) - 30 + "px")
            .style("left", Xscale(i.genra) + 100 + "px");
        })
        .on("mousemove", function (event, d) {
          return tooltip
            .style("visibility", "visible")
            .style("top", d3.pointer(this)[0] + 10 + 20 + "px")
            .style("left", event.pageX - 80 + "px");
        })
        .on("mouseout", function () {
          return tooltip.style("visibility", "hidden");
        })
        .transition()
        .duration(1100)
        .attr("y", (d, i) => Yscale(d.rating))
        .attr("height", (d) => graph_h - 300 - Yscale(d.rating));

      // append a group element that contains X-axis to the svg group element
      const Xaxis = g
        .append("g")
        .call(d3.axisBottom(Xscale))
        .attr("transform", `translate(0,${innerWidth - 100})`)
        .append("text")
        .attr("dy", 50)
        .attr("dx", graph_w / 4)
        .attr("text-anchor", "start")
        .attr("font-size", "30px")
        .attr("stroke", "steelblue")
        .attr("font-family", "Gill Sans, sans-serif")
        .attr("fill", "steelblue")
        .text("Genre");

      // append a group element that contains Y-axis to the svg group element
      const Yaxis = g
        .append("g")
        .call(d3.axisLeft(Yscale).ticks(d3.max(Yscale.domain()) * 2))
        .attr("transform", `translate(0,${innerHeight - 100})`)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left - 5)
        .attr("x", -graph_h / 5)
        .attr("dy", 20)
        .attr("dx", -10)
        .attr("text-anchor", "end")
        .attr("font-size", "20px")
        .attr("stroke", "steelblue")
        .attr("font-family", "Gill Sans, sans-serif")
        .attr("fill", "steelblue")
        .text("Rating");
    }
  }

  graph();