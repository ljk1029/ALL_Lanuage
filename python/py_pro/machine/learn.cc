#include <iostream>
#include <vector>

// 定义线性回归模型
class LinearRegression {
public:
    // 构造函数，初始化模型参数
    LinearRegression() : theta0(0.0), theta1(0.0) {}

    // 使用梯度下降算法训练模型
    void train(const std::vector<double>& X, const std::vector<double>& y, double learning_rate, int num_iterations) {
        int m = X.size();
        for (int iter = 0; iter < num_iterations; ++iter) {
            double sum0 = 0.0;
            double sum1 = 0.0;
            for (int i = 0; i < m; ++i) {
                double prediction = predict(X[i]);
                double error = prediction - y[i];
                sum0 += error;
                sum1 += error * X[i];
            }
            theta0 -= learning_rate * (1.0 / m) * sum0;
            theta1 -= learning_rate * (1.0 / m) * sum1;
        }
    }

    // 使用模型进行预测
    double predict(double x) const {
        return theta0 + theta1 * x;
    }

private:
    double theta0; // 模型参数 theta0
    double theta1; // 模型参数 theta1
};

int main() {
    // 训练数据：自变量 X 和因变量 y
    std::vector<double> X = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> y = {2.0, 4.0, 5.0, 4.0, 5.5};

    // 创建线性回归模型
    LinearRegression model;

    // 使用梯度下降算法训练模型
    double learning_rate = 0.01;
    int num_iterations = 1000;
    model.train(X, y, learning_rate, num_iterations);

    // 使用模型进行预测
    double x_test = 6.0;
    double y_pred = model.predict(x_test);
    std::cout << "预测结果:y = " << y_pred << std::endl;

    return 0;
}
