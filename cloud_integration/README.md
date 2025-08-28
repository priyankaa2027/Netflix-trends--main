# Netflix Trends Power BI Cloud Integration

## Project Overview
This project uses Power BI to visualize Netflix trends using the provided Excel dataset. The dashboard is cloud-integrated for automatic data refresh and sharing.

## Steps to Integrate with Cloud
1. **Upload Data to Cloud Storage**
   - Place `fully_cleaned_netflix_dataset.xlsx` in OneDrive or SharePoint.
2. **Connect Power BI to Cloud Data**
   - In Power BI Desktop, use `Get Data > Web` or `Get Data > SharePoint Folder` to connect to the cloud file.
   - Use the cloud URL for the Excel file.
3. **Publish to Power BI Service**
   - Publish the `.pbix` file to Power BI Service.
   - Set up scheduled refresh using the cloud data source.
4. **Share Dashboard**
   - Share the dashboard with stakeholders via Power BI Service.

## Connect Power BI to Cloud MongoDB (MongoDB Atlas)
1. **Set Up MongoDB Atlas**
   - Create a free cluster at https://www.mongodb.com/cloud/atlas.
   - Load your Netflix dataset into a MongoDB collection.
2. **Install MongoDB BI Connector or ODBC Driver**
   - Use the official [MongoDB BI Connector](https://www.mongodb.com/products/bi-connector) or [ODBC Driver](https://www.mongodb.com/docs/bi-connector/odbc/) to enable SQL access to MongoDB.
3. **Connect Power BI to MongoDB**
   - In Power BI Desktop, go to `Get Data > ODBC`.
   - Select the DSN configured for your MongoDB Atlas cluster.
   - Import and model your data as needed.
4. **Publish and Schedule Refresh**
   - Publish your dashboard to Power BI Service.
   - Configure scheduled refresh using the ODBC connection.

### Step-by-Step: Connecting MongoDB Atlas to Power BI
1. Log in to MongoDB Atlas and navigate to your cluster.
2. Click 'Connect', choose 'Drivers', and select 'ODBC'.
3. Copy your connection string (format: `mongodb+srv://<username>:<password>@<cluster-url>/<database>?authSource=admin`).
4. Download and install the MongoDB ODBC Driver: https://www.mongodb.com/docs/bi-connector/odbc/
5. Open 'ODBC Data Source Administrator' on Windows and add a new DSN using the MongoDB ODBC driver.
6. Enter your connection string, username, and password in the DSN setup.
7. In Power BI Desktop, go to 'Get Data > ODBC', select your DSN, and connect.
8. Load your data and build your dashboard.

#### Sample MongoDB Atlas ODBC Connection String
```
mongodb+srv://<username>:<password>@<cluster-url>/<database>?authSource=admin
```
Replace `<username>`, `<password>`, `<cluster-url>`, and `<database>` with your actual details.

## Automation (Optional)
- Use the provided PowerShell script to automate data refresh or file uploads.

## Resources
- [Power BI Cloud Refresh Documentation](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem)
- [OneDrive Integration](https://learn.microsoft.com/en-us/power-bi/connect-data/service-connect-to-files-onedrive-business)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [MongoDB BI Connector](https://www.mongodb.com/products/bi-connector)
- [MongoDB ODBC Driver](https://www.mongodb.com/docs/bi-connector/odbc/)
