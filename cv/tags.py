all_tags_list = list(set([
    # Programming Languages
    'Python', 'Java', 'C++', 'C#', 'JavaScript', 'TypeScript', 'Ruby', 'Go', 'Rust', 'Swift', 'Kotlin',
    'PHP', 'Perl', 'Scala', 'Haskell', 'Elixir', 'Clojure', 'R', 'Matlab', 'Objective-C', 'VB.NET', 'Groovy',
    'Dart', 'Lua', 'Shell', 'PowerShell', 'Assembly', 'COBOL', 'Fortran', 'Pascal',

    # Frontend Frameworks and Libraries
    'React', 'Angular', 'Vue.js', 'Svelte', 'Next.js', 'Nuxt.js', 'jQuery', 'Bootstrap', 'Tailwind CSS',
    'Foundation', 'Bulma', 'Semantic UI', 'Material-UI', 'Ember.js', 'Backbone.js', 'Alpine.js',

    # Backend Frameworks and Libraries
    'Node.js', 'Express', 'Django', 'Flask', 'Spring', 'Rails', 'Laravel', 'ASP.NET', 'Phoenix', 'Sinatra',
    'Koa', 'Fastify', 'NestJS', 'Hapi', 'Gin', 'Fiber', 'FastAPI', 'Pyramid', 'Tornado',

    # Databases
    'MySQL', 'PostgreSQL', 'SQLite', 'MongoDB', 'Cassandra', 'Redis', 'Elasticsearch', 'DynamoDB', 'CouchDB',
    'MariaDB', 'Oracle DB', 'SQL Server', 'Neo4j', 'HBase', 'Memcached', 'InfluxDB', 'Firebird', 'RethinkDB',

    # Cloud Services and Platforms
    'AWS', 'Azure', 'Google Cloud', 'Heroku', 'Netlify', 'DigitalOcean', 'Linode', 'Vultr', 'IBM Cloud',
    'Oracle Cloud', 'Firebase', 'Kubernetes', 'OpenShift', 'CloudFoundry', 'Alibaba Cloud', 'Tencent Cloud',

    # AWS Services
    'AWS EC2', 'AWS S3', 'AWS RDS', 'AWS Lambda', 'AWS DynamoDB', 'AWS CloudFormation', 'AWS CloudWatch', 'AWS IAM',
    'AWS ECS', 'AWS EKS', 'AWS Fargate', 'AWS Elastic Beanstalk', 'AWS SQS', 'AWS SNS', 'AWS Kinesis', 'AWS Glue',
    'AWS Redshift', 'AWS EMR', 'AWS SageMaker', 'AWS Step Functions', 'AWS AppSync', 'AWS Amplify',

    # Azure Services
    'Azure App Service', 'Azure Functions', 'Azure SQL Database', 'Azure Blob Storage', 'Azure DevOps',
    'Azure Kubernetes Service', 'Azure Cosmos DB', 'Azure Active Directory', 'Azure Logic Apps', 'Azure Synapse',
    'Azure Machine Learning', 'Azure Data Factory', 'Azure Service Bus', 'Azure Event Hubs',

    # Google Cloud Services
    'Google Cloud Functions', 'Google Cloud Storage', 'Google BigQuery', 'Google App Engine', 'Google Kubernetes Engine',
    'Google Cloud Pub/Sub', 'Google Cloud SQL', 'Google Cloud Spanner', 'Google Cloud Firestore', 'Google Dataflow',
    'Google Dataproc', 'Google AI Platform', 'Google Cloud Run', 'Google Cloud Build', 'Google Cloud Armor',

    # DevOps and CI/CD
    'Docker', 'Kubernetes', 'Terraform', 'Ansible', 'Jenkins', 'Travis CI', 'CircleCI', 'GitLab CI/CD',
    'GitHub Actions', 'Bamboo', 'TeamCity', 'Argo CD', 'Spinnaker', 'Puppet', 'Chef', 'SaltStack', 'Vault',

    # Version Control and Collaboration
    'Git', 'GitHub', 'GitLab', 'Bitbucket', 'SVN', 'Mercurial', 'Perforce', 'SourceForge',

    # Agile and Project Management
    'Agile', 'Scrum', 'Kanban', 'JIRA', 'Trello', 'Asana', 'Monday.com', 'ClickUp', 'Notion', 'Basecamp', 'Pivotal Tracker',

    # UI/UX Design Tools
    'Figma', 'Sketch', 'Adobe XD', 'InVision', 'Framer', 'Marvel', 'Balsamiq', 'Axure', 'Adobe Photoshop', 'Adobe Illustrator',

    # UI/UX Processes
    'User Research', 'Wireframing', 'Prototyping', 'Usability Testing', 'Interaction Design', 'Information Architecture',
    'Visual Design', 'Design Systems', 'User Personas', 'Journey Mapping',

    # Data Analysis and Visualization
    'Data Analysis', 'Data Visualization', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Plotly', 'D3.js', 'ggplot2', 'Bokeh',
    'Tableau', 'Power BI', 'QlikView', 'Looker', 'Grafana', 'Kibana',

    # Machine Learning and AI
    'Machine Learning', 'Deep Learning', 'TensorFlow', 'Keras', 'PyTorch', 'Scikit-learn', 'XGBoost', 'LightGBM', 'CatBoost',
    'H2O.ai', 'Apache MXNet', 'Caffe', 'Theano', 'CNTK', 'Torch', 'Fastai',

    # Natural Language Processing
    'Natural Language Processing', 'Spacy', 'NLTK', 'Gensim', 'BERT', 'GPT-3', 'Transformer', 'seq2seq', 'OpenNMT', 'AllenNLP',

    # Computer Vision
    'Computer Vision', 'OpenCV', 'Detectron2', 'YOLO', 'SSD', 'Faster R-CNN', 'Mask R-CNN', 'DeepFace', 'FaceNet',

    # Big Data Technologies
    'Big Data', 'Hadoop', 'Spark', 'Kafka', 'Flink', 'Hive', 'Pig', 'Druid', 'Presto', 'Storm', 'Samza',

    # Mathematics and Statistics
    'Statistics', 'Probability', 'Linear Algebra', 'Calculus', 'Discrete Mathematics', 'Combinatorics', 'Graph Theory',

    # Project and Product Management
    'Project Management', 'Product Management', 'Stakeholder Management', 'Risk Management', 'Change Management',
    'Requirement Gathering', 'User Stories', 'Backlog Prioritization', 'Roadmapping', 'Sprint Planning', 'Scrum Master',

    # Testing and Quality Assurance
    'Unit Testing', 'Integration Testing', 'End-to-End Testing', 'Behavior-Driven Development', 'Test-Driven Development',
    'Jest', 'Mocha', 'Chai', 'Cypress', 'Selenium', 'Appium', 'JUnit', 'TestNG', 'PyTest', 'Robot Framework', 'Cucumber',

    # Mobile Development
    'Mobile Development', 'iOS', 'Android', 'React Native', 'Flutter', 'Swift', 'Kotlin', 'Objective-C', 'Java for Android',
    'Xamarin', 'Ionic', 'Cordova', 'PhoneGap', 'NativeScript',

    # Security and Compliance
    'Security', 'Encryption', 'Authentication', 'Authorization', 'Penetration Testing', 'OWASP', 'SSL/TLS', 'OAuth',
    'JWT', 'SSO', 'Firewall', 'Intrusion Detection', 'Intrusion Prevention', 'SIEM', 'SOC', 'GDPR', 'HIPAA', 'PCI DSS',

    # Performance and Optimization
    'Performance Optimization', 'Scalability', 'Load Balancing', 'Caching', 'CDN', 'Profiling', 'Stress Testing',
    'Benchmarking', 'APM', 'New Relic', 'Dynatrace', 'AppDynamics',

    # Cloud Computing and Serverless
    'Cloud Computing', 'Serverless Architecture', 'Microservices', 'API Gateway', 'Service Mesh', 'Istio', 'Linkerd',

    # Other Tools and Technologies
    'AR/VR', 'Game Development', 'Unity', 'Unreal Engine',
    'Blockchain', 'Cryptocurrency', 'Smart Contracts', 'Ethereum', 'Solidity', 'Hyperledger', 'Corda',
    'Robotic Process Automation', 'UiPath', 'Automation Anywhere', 'Blue Prism'
]))

