def generate_gantt_chart_html(tasks):
    # 创建HTML文件并写入基本结构
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gantt Chart</title>
        <script src="https://d3js.org/d3.v6.min.js"></script>
    </head>
    <body>
        <svg width="1000" height="400"></svg>
        <script>
    """

    # 添加D3.js代码
    js_content = """
            const tasks = [
    """

    for task in tasks:
        js_content += """
                {{ "name": "{name}", "start": new Date("{start}"), "end": new Date("{end}") }},
        """.format(name=task["name"], start=task["start"], end=task["end"])

    js_content += """
            ];

            const margin = {top: 20, right: 30, bottom: 30, left: 40};
            const width = 1000 - margin.left - margin.right;
            const height = 400 - margin.top - margin.bottom;

            const svg = d3.select("svg")
                        .attr("width", width + margin.left + margin.right)
                        .attr("height", height + margin.top + margin.bottom)
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            const x = d3.scaleTime()
                    .domain([d3.min(tasks, d => d.start), d3.max(tasks, d => d.end)])
                    .range([0, width]);

            const y = d3.scaleBand()
                    .domain(tasks.map(d => d.name))
                    .range([0, height])
                    .padding(0.1);

            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            svg.append("g")
                .call(d3.axisLeft(y));

            svg.selectAll("rect")
                .data(tasks)
                .enter()
                .append("rect")
                .attr("x", d => x(d.start))
                .attr("y", d => y(d.name))
                .attr("width", d => x(d.end) - x(d.start))
                .attr("height", y.bandwidth())
                .attr("fill", "steelblue");
        </script>
    </body>
    </html>
    """

    # 合并HTML和JavaScript内容
    html_content += js_content

    # 将内容写入HTML文件
    with open("gantt_chart.html", "w") as f:
        f.write(html_content)


# 示例任务数据
tasks = [
    {"name": "Task 1", "start": "2024-05-01", "end": "2024-05-05"},
    {"name": "Task 2", "start": "2024-05-03", "end": "2024-05-08"},
    {"name": "Task 3", "start": "2024-05-06", "end": "2024-05-10"},
    # 添加更多任务
]

# 生成甘特图HTML文件
generate_gantt_chart_html(tasks)
