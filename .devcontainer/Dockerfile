# Start with Debian
FROM debian:bullseye-slim


# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    apt-transport-https \ 
    lsb-release \ 
    gnupg2 \
    tree \ 
    jq\ 
    openjdk-11-jre \
    procps

# Install Docker CLI
RUN curl -fsSLk https://download.docker.com/linux/debian/gpg | apt-key add - \
    && echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-ce-cli

# Install Python 3.9
RUN apt-get install -y python3.9

# Install Pandas
RUN apt-get install -y python3-pip && pip3 install pandas
RUN apt-get update && apt-get install -y git

# Install Spark
RUN wget -q https://downloads.apache.org/spark/spark-3.4.2/spark-3.4.2-bin-hadoop3.tgz -O /tmp/spark.tgz \
    && tar -xzf /tmp/spark.tgz -C /opt \
    && mv /opt/spark-3.4.2-bin-hadoop3 /opt/spark \
    && rm /tmp/spark.tgz

# Set Spark Environment Variables
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

RUN wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list && \
    apt update

CMD ["/bin/bash"]

