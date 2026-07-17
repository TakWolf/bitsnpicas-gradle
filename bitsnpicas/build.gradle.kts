plugins {
    java
    application
    id("com.gradleup.shadow")
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}

application {
    mainClass = "com.kreative.bitsnpicas.main.Main"
}

dependencies {
    implementation(project(":unicode"))
}

tasks.shadowJar {
    archiveBaseName = "BitsNPicas"
    archiveClassifier = ""
    destinationDirectory = rootProject.layout.buildDirectory.dir("releases")
}
