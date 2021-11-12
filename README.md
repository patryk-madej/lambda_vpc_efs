1. Install Serverless:

npm install -g serverless

OR

curl -o- -L https://slss.io/install | bash

OR (on Windows)

choco install serverless


2. Install plugins:

serverless plugin install --name serverless-lift

serverless plugin install --name serverless-vpc-plugin


3. Configure your user credentials:

serverless config credentials --provider aws --key 1234 --secret 5678
