# A Java/Maven/JUnit/CI HelloWorld example to test in myusine

## new section
This example demonstrates:
* A simple Java 8 application with tests
* Unit tests written with [JUnit 5](https://junit.org/junit5/)
* Integration tests written with [JUnit 5](https://junit.org/junit5/)
* Code coverage reports via [JaCoCo](https://www.jacoco.org/jacoco/)
* A Maven build that puts it all together
* modif dev 1
* modif dev 2

## modif feature1
* sub feature1


## Running the tests

* To run the unit tests, call `mvn test`
* To run the integration tests as well, call `mvn verify`
* Code coverage reports are generated when `mvn verify` (or a full `mvn clean install`) is called.
  Point a browser at the output in `target/site/jacoco-both/index.html` to see the report.

## Conventions

This example follows the following basic conventions:

| | unit test | integration test |
| --- | --- | --- |
| **resides in:** | `src/test/java/*Test.java` | `src/test/java/*IT.java` |
| **executes in Maven phase:** | test | verify |
| **handled by Maven plugin:** | [surefire](http://maven.apache.org/surefire/maven-surefire-plugin/) | [failsafe](http://maven.apache.org/surefire/maven-failsafe-plugin/) |

# How to deploy Maven projects to Nexus with GitLab CI/CD

## Introduction

In this project, we show how you can leverage the power of [GitLab CI/CD](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/)
to build a [Maven](https://maven.apache.org/) project and deploy it to [Nexus](https://nexus.bio.di.uminho.pt/).

You'll use this project as example to test Gitlab CI using Maven and our Nexus.

We assume that you already have a GitLab account on [gitLab.bio.di.uminho.pt](http://gitlab.bio.di.uminho.pt/), and that you know the basic usage of Git and [GitLab CI/CD](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/).
We also assume that the Nexus is available and reachable from the internet, and that you have valid credentials to deploy on it. (Please ask for your Nexus credentials from our Servers/Resources Administrators) 

## Create the Project

First, you need an application to work with: in this specific case we'll use a
simple one, but it could be any Maven application. This will be the dependency
you want to package and deploy to Nexus, to be available to other
projects.

### Prepare the dependency application

For this article you'll use a Maven app that can be cloned from our example
project:

1. Log in to your GitLab account
1. Create a new project by selecting **Import project from > Repo by URL**
1. Add the following URL:

   ```plaintext
   https://gitlab.bio.di.uminho.pt/tutorials/java-maven-junit-ci-helloworld.git
   ```

1. Click **Create project**

This application is nothing more than two basic classes with some JUnits.

The project structure is really simple, and you should consider these two resources:

- `pom.xml`: project object model (POM) configuration file
- `src/main/java/com/example/javamavenjunithelloworld/HelloApp.java`: main of our application

### Configure the Nexus deployment for Snaspshots

The application is ready to use, but you need some additional steps to deploy it to Nexus:

1. Log in to Nexus with your user's credentials.
1. From the main screen, click on the `Snapshots` item in the **Repositories** panel.
1. Copy to clipboard the configuration snippet under the **Summary** Tab.
1. Change the `url` value to have it configurable by using variables.
1. Copy the snippet in the `pom.xml` file for your project, just after the
   `dependencies` section. The snippet should look like this:

   ```xml
   <distributionManagement>
     <repository>
       <id>snapshots</id>
       <url>${MAVEN_REPO_URL}/content/repositories/snapshots</url>
     </repository>
   </distributionManagement>
   ```

Another step you need to do before you can deploy the dependency to Nexus
is to configure the authentication data. It is a simple task, but Maven requires
it to stay in a file called `settings.xml` that has to be in the `.m2` subdirectory
in the user's homedir.

Since you want to use a runner to automatically deploy the application, you
should create the file in the project's home directory and set a command line
parameter in `.gitlab-ci.yml` to use the custom location instead of the default one:

1. Create a folder called `.m2` in the root of your repository
1. Create a file called `settings.xml` in the `.m2` folder
1. Copy the following content into a `settings.xml` file:

   ```xml
   <settings xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.1.0 http://maven.apache.org/xsd/settings-1.1.0.xsd"
       xmlns="http://maven.apache.org/SETTINGS/1.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <servers>
       <server>
         <id>releases</id>
         <username>${MAVEN_REPO_USER}</username>
         <password>${MAVEN_REPO_PASS}</password>
       </server>
       <server>
         <id>snapshots</id>
         <username>${MAVEN_REPO_USER}</username>
         <password>${MAVEN_REPO_PASS}</password>
       </server>
     </servers>
   </settings>
   ```

    Username and password will be replaced by the correct values using variables.

### Configure GitLab CI/CD 

Now it's time we set up [GitLab CI/CD](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/) to automatically build, test and deploy the dependency!

GitLab CI/CD uses a file in the root of the repository, named `.gitlab-ci.yml`, to read the definitions for jobs
that will be executed by the configured runners. You can read more about this file in the [GitLab Documentation](https://docs.gitlab.com/ee/ci/yaml/README.md).

First of all, remember to set up variables for your deployment. Navigate to your project's **Settings > CI/CD > Environment variables** page
and add the following ones (replace them with your current values, of course):

- **MAVEN_REPO_URL**: `https://nexus.bio.di.uminho.pt` (our Nexus URL)
- **MAVEN_REPO_USER**: `nexususer` (your Nexus username)
- **MAVEN_REPO_PASS**: `nexuspassword` (your Nexus Password)

Now it's time to define jobs in `.gitlab-ci.yml` and push it to the repository:

```yaml
image: maven:3.6-jdk-8-slim

variables:
  MAVEN_CLI_OPTS: "-s .m2/settings.xml --batch-mode"
  MEVEN_DEPLOY_OPTS: "-DskipTests"
  MAVEN_OPTS: "-Dmaven.repo.local=.m2/repository"

cache:
  paths:
    - .m2/repository/
    - target/

build:
  stage: build
  script:
    - mvn $MAVEN_CLI_OPTS compile

test:
  stage: test
  script:
    - mvn $MAVEN_CLI_OPTS test

deploy:
  stage: deploy
  script:
    - mvn $MAVEN_CLI_OPTS deploy $MEVEN_DEPLOY_OPTS
  only:
    - master
    - dev
```

The runner uses the latest [Maven Docker image](https://hub.docker.com/_/maven/),
which contains all of the tools and dependencies needed to manage the project
and to run the jobs.

Environment variables are set to instruct Maven to use the `homedir` of the repository instead of the user's home when searching for configuration and dependencies.

Caching the `.m2/repository folder` (where all the Maven files are stored), and the `target` folder (where our application will be created), is useful for speeding up the process
by running all Maven phases in a sequential order, therefore, executing `mvn test` will automatically run `mvn compile` if necessary.

Both `build` and `test` jobs leverage the `mvn` command to compile the application and to test it as defined in the test suite that is part of the application.

Deploy to Nexus is done as defined by the variables we have just set up.
The deployment occurs only if we're pushing or merging to `master` branch, so that the development versions are tested but not published.

Done! Now you have all the changes in the GitLab repository, and a pipeline has already been started for this commit. In the **Pipelines** tab you can see what's happening.
If the deployment has been successful, the deploy job log will output:

```plaintext
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.983 s
```

>**Note**:
the `mvn` command downloads a lot of files from the internet, so you'll see a lot of extra activity in the log the first time you run it.

Yay! You did it! Checking in Nexus will confirm that you have a new artifact available in the `Snapshots` repository.


### Configure the Nexus deployment for Releases

Attention, this step will replace the configurations for snapshots to releases in master branch. 
Its advised to have a `dev` branch to deploy snapshots (just clone the master branch to the dev branch).

The application is ready to deploy snapshots in the master branch, but now you need some additional steps to deploy it as release to Nexus:

1. Log in to Nexus with your user's credentials.
1. From the main screen, click on the `Releases` item in the **Repositories** panel.
1. Copy to clipboard the configuration snippet under the **Summary** Tab.
1. Change the `url` value to have it configurable by using variables.
1. Copy the snippet in the `pom.xml`, replace the
   `distributionManagement` section. The snippet should look like this:

   ```xml
   <distributionManagement>
     <repository>
       <id>releases</id>
       <url>${MAVEN_REPO_URL}/content/repositories/releases</url>
     </repository>
   </distributionManagement>
   ```
1. Change `version` in the `pom.xml` without `-SNAPSHOT` and commit into master branch. 


Yay, after these changes the CI will deploy a release version of your java application!
Checking in Nexus will confirm that you have a new artifact available in the `Releases` repository.
>**Note**:
Be aware that Nexus doesn't allow replacements of the same version of a java package release without Nexus Administrator authorization!

## Converting JaCoCo Integration reports into Gitlab Cobertura
This project contains JaCoCo integration reports that can be converted into Gitlab cobertura.
To enable this integration test, you must add the missing jobs to `.gitlab-ci.yml` file described in this link:
 ```plaintext
https://docs.gitlab.com/ee/user/project/merge_requests/test_coverage_visualization.html   
 ```

## Conclusion

In this article we covered the basic steps to use the Nexus Maven repository to automatically publish and consume artifacts.

A similar approach could be used to interact with any other Maven compatible Binary Repository Manager.
Obviously, you can improve these examples, optimizing the `.gitlab-ci.yml` file to better suit your needs, and adapting to your workflow.
