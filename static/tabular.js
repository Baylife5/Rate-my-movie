fetch("/static/tabular.json")
    .then((res) => res.json())
    .then((tabledata) => {
        //initialize table
        var table = new Tabulator("#table", {
        data: tabledata,
        layout: "fitDataTable",
        height: "510px",
        renderHorizontal: "virtual",
        columns: [
            { title: "Reviewer", field: "reviewer" },
            { title: "Title", field: "title" },
            { title: "Release Data", field: "release date" },
            { title: "Genre", field: "genre" },
            { title: "Rating", field: "rating", sorter: "number" },
        ],
        });
    })
    .catch((error) => {
        console.error("Error fetching data:", error);
    });