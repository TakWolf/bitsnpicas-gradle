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
    mainClass = "com.kreative.mapedit.Main"
}

dependencies {
    implementation(project(":unicode"))
}
