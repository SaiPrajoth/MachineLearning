

Multiple Linear Regression (Brief Definition):
Multiple linear regression is a supervised machine learning method used to model the relationship between a dependent variable (target) and multiple independent variables (features) by fitting a linear equation to the observed data. It aims to find the best-fitting hyperplane that minimizes the error between predicted and actual values.

Data:
   - Definition: Data consists of pairs of input features (X₁, X₂, ..., Xₙ) and corresponding target values (Y) used for model training and testing.
   - Example: In predicting house prices, data may include features like square footage, number of bedrooms, and bathrooms (X₁, X₂, X₃) along with actual house prices (Y) for various houses.

Gradient Descent:
   - Definition: Gradient descent is the optimization algorithm used to adjust the model's parameters (θ₀, θ₁, θ₂, ..., θₙ) to minimize the cost function. In multiple linear regression, we have a gradient descent equation for each parameter:
     ```
     θⱼ = θⱼ - α * ∂J(θ)/∂θⱼ for j = 0 to n
     ```
     - α is the learning rate, controlling the step size.
     - ∂J(θ)/∂θⱼ is the partial derivative of the cost function with respect to θⱼ.

Cost Function (Mean Squared Error):
   - Definition: The cost function measures how well the model's predictions (Y_pred) match the actual target values (Y) for the given input features. In multiple linear regression, we use the Mean Squared Error (MSE) cost function:
     ```
     J(θ) = (1/2m) * Σ(Y_pred - Y)² for i = 1 to m
     ```
     - J(θ) represents the cost to be minimized.
     - m is the number of data points.
     - Y_pred is the predicted target value.
     - Y is the actual target value.

Mean Squared Error (MSE):
   - Definition: MSE is a specific cost function used in multiple linear regression. It calculates the average of the squared differences between the predicted target values (Y_pred) and the actual target values (Y) for all data points in the dataset:
     ```
     MSE = (1/m) * Σ(Y_pred - Y)² for i = 1 to m
     ```
     - Y_pred represents the predicted target value.
     - Y represents the actual target value.
     - The sum is taken over all data points in the dataset.

In summary, in the context of multiple linear regression:
- Data involves input features and target values.
- Gradient Descent adjusts model coefficients (θ₀, θ₁, θ₂, ..., θₙ) to minimize the cost function.
- Cost Function (MSE) measures the alignment of model predictions with actual values.
- Mean Squared Error (MSE) quantifies the average squared difference between predicted and actual target values for multiple input features.
