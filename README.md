# Upload libraries to Lambda

1. Create folder `python`
```
mkdir python
cd python
```

2. Download libraries to this folder
```
pip3 install apiclient -t .
```

3. Zip folder. Example: python.zip

4. Login to AWS Lambda and go to **Layers**.

5. Click on `Create Layer`. Fill up name, upload zip file and select compatible runtimes (Python 3.9, 3.8 and 3.7). Then, click **Create** button.

6. Then switch to Functions and select **your target function**.

7. Click on the **Layers** button below the function icon and click on **Add a layer**.

8. Click on **Custom layers** and select the library layer created from the dropdown and the respective version. Then, click **Add**.

9. Then, run your app.
