# Setup guide for this project

## Nativescript Vue

From cmd install globally:

npm install -g @vue/cli @vue/cli-init

More info: [NativeScript Vue Quick Start](https://nativescript-vue.org/en/docs/getting-started/quick-start/)


## Android emulator

### Note: There is probably a way without downloading the whole Android Studio

Download Android Studio

Create AVD with Android v 9.0 following this: [https://developer.android.com/studio/run/managing-avds.html](https://developer.android.com/studio/run/managing-avds.html)

Download Android v 9.0 SDK

Create ANDROID_HOME env. variable and add path to sdk

![android_home](https://bitbucket.org/repo/d5oBa4G/images/1755990179-e76a3f8b3054697dd7ae879718dfec6d.png)

Add similar paths to PATH variable

![path var](https://bitbucket.org/repo/d5oBa4G/images/675575499-bdda03d2a9c04955d9284938694ed6ea.png)

Open App folder with CMD

Run the created android AVD with android studio

```
#!cmd

tns run android

```

Note that after the initial setup you do not need to run the AVD from Android Studio separately, just use tns run android.

## Physical smartphone testing:

Install Nativescript Playground and Nativescript Preview apps from App Store or Google Play

From terminal in App folder: 
```
#!cmd

tns preview
```
Scan QR code with NativeScript Playground app.


## Useful extentions for VSCode:

* Vetur - text highlighting and code completion
* NativeScript - general nativescript support
* Better Comments

## Other