import pymysql


class MySQLDemoPipeline:
    def __init__(self):
        ## Connection Details
        hostname = "localhost"
        username = "root"
        password = "root"  # your password
        database = "book-test1"

        ## Create/Connect to database
        self.connection = pymysql.connect(
            host=hostname,
            user=username,
            password=password,
            db=database,
            cursorclass=pymysql.cursors.DictCursor,
        )

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        ## Create quotes table if none exists
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS quotes(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR(255),
            category VARCHAR(255),
            description VARCHAR(255)
        )
        """
        )

    def process_item(self, item, spider):
        # Define insert statement
        self.cur.execute(
            """ insert into quotes (title, category, description) values (%s,%s,%s)""",
            (item["title"], str(item["category"]), item["description"]),
        )

        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()
