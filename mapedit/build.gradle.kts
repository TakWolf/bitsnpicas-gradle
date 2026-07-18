plugins {
    java
    application
    id("com.gradleup.shadow")
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

application {
    mainClass = "com.kreative.mapedit.Main"
}

dependencies {
    implementation(project(":unicode"))
}

tasks.shadowJar {
    archiveBaseName = "MapEdit"
    archiveClassifier = ""
    destinationDirectory = rootProject.layout.buildDirectory.dir("releases")
}
