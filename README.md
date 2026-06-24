# CS-340-Client-Server-Development-
How do you write programs that are maintainable, readable, and adaptable?

I write programs that are maintainable, readable, and adaptable by organizing code into separate modules and using clear naming conventions. In Project One, I created a CRUD Python module that handled all communication between the dashboard and the MongoDB database. Separating the database operations from the dashboard code made the project easier to understand and maintain because changes to the database connection or queries could be made in one location without affecting the rest of the application.

One advantage of using the CRUD module was code reusability. Instead of rewriting database functions multiple times, I was able to call the same methods throughout the project. This approach also reduced errors and made debugging easier. In the future, I could reuse this CRUD module in other applications that need to connect to a MongoDB database, including inventory systems, customer management applications, or data analysis dashboards.

How do you approach a problem as a computer scientist?

When approaching a problem as a computer scientist, I first analyze the requirements and break the project into smaller tasks. For the Grazioso Salvare dashboard project, I started by understanding the database structure and determining how the data needed to be displayed for the client. After creating the database connection, I built the dashboard components one step at a time and tested each feature before moving to the next.

This approach differed from some previous assignments because it required integrating multiple technologies, including Python, MongoDB, Dash, and data visualization tools. Rather than focusing on a single program, I had to consider how different systems worked together. In the future, I would continue using a structured development process that includes planning, testing, and modular design when creating databases and applications that meet client requirements.

What do computer scientists do, and why does it matter?

Computer scientists design, develop, and improve software systems that help organizations solve problems and make better decisions. Their work matters because businesses rely on technology to manage data, improve efficiency, and provide services to customers.

This project demonstrated how software can help an organization like Grazioso Salvare manage and analyze large amounts of animal rescue data. By creating a dashboard that allows users to filter information and view data visually, the organization can make faster and more informed decisions. Projects like this show how computer science can transform raw data into useful information that supports business goals and improves overall operations.
