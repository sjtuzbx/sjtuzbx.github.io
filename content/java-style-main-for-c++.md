Title: C++ 如何实现Java风格的c++入口函数
Date: 2023-12-30 9:30
Category: programming
Tags: programing
Author: sjtuzbx
Summary: 我们知道所有的程序都有一个`Main`入口函数，C++风格的入口函数是这样的.

我们知道所有的程序都有一个`Main`入口函数，C++风格的入口函数是这样的.

```c++
int main(int argc, char *argv[]) {
    // your code here
    return 0;
}
```

而Java中则是面向对象风格的`Main`入口函数.
```java
public class HelloApp {
    public static void main(String[] args) {
        // your code here 
    }
}
```

那么我们如果也希望在C++中实现类似面向对象风格的入口函数可以怎么做呢？

这里可以借助`宏`来实现, 首先新建一个`app.hpp`的头文件用于保存我们相关的`宏`

```c++
// app.hpp

class app {
public:
  app(int argc, char **argv) {
  }

  app(const app &) = delete;
  app &operator=(const app  &) = delete;
  ~app() {}

  virtual void run() {}
};

#ifndef LAUNCH_APP
#define LAUNCH_APP(launcher)                                                   \
  std::unique_ptr<launcher> app;                                               \
  int main(int argc, char **argv) {                                            \
    app.reset(new launcher(argc, argv));                                       \
    app->run();                                                                \
    app.reset();                                                               \
    return 0;                                                                  \
  }
#endif
```

我们可以定义这样一个基类`app`和宏`LAUNCH_APP`, 将原先c++风格的main函数包在宏中。然后当我们每次写一个新程序时，就可以使用面向对象风格的Main入口函数了.

```c++
// main.cpp

#include <iostream>
#include "app.hpp"

class hello_world : public infra::app {
public:
    hello_world(int argc, char **argv)
        :app(argc, argv) {
    
    }

    void run() override {
        std::cout << "Hello world" << std::endl;
    }
};

LAUNCH_APP(hello_world)
```

我们只需要专注于`run()`函数的实现就行~

后续还可以进一步扩展基类app，比如添加`log`,`thread`和异常处理等额外功能~

