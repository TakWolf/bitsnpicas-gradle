plugins {
    java
    application
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
