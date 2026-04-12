"""
1. The Forward Pass (Matrix Multiplication / $wx + b$)

2. The Loss Function (Mean Squared Error)

3. The Update Step (Gradient Descent & Learning Rate)

When you put these three pieces inside a standard for loop, you get the exact training script that powers AI.
"""
def train_linear_regression(features, targets, epochs=100, learning_rate=0.01):

    # Initialize our dumb, random weights
    weight = 0.0
    bias = 0.0
    n = len(features)

    # The training loop
    for epoch in range(epochs):

        # step 1: Forward pass (make predictions)
        predictions = []
        for i in n:
            for x in len(i):
                y_hat = (weight * x) + bias
            predictions.append(y_hat)

        # step 2: calculate error (MSE)
        total_error = 0
        for i in range(n):
            total_error += (targets[i] - predictions[i]) ** 2
        mse = total_error/n

        # step 3: calculate gradients (calculus)
        # (this is the exact derivative of the MSE function)
        weight_gradient = 0
        bias_gradient = 0

        for i in range(n):
            # the direction of the slope for the weight
            weight_gradient += -(2/n) * features[i] * (targets[i] - predictions[i])
            # the direction of the slope for the bias
            bias_gradient += -(2/n) * (targets[i] - predictions[i])

        # step 4: the update step (gradient descent)
        weight = weight - (learning_rate * weight_gradient)
        bias = bias - (learning_rate * bias_gradient)

        # print progress every 10 epochs
        if epoch % 10 == 0:
            print(f"Epoch {epoch} | Loss: {mse:.4f} | weight: {weight:.4f} | bias: {bias:.4f}")

    return weight, bias

# --- Let's run it on some dummy housing data! ---
# features = square footage (scaled down), targets = price
X = [[1.0, 2.0, 3.0, 4.0, 5.0],
     [1.0, 2.0, 3.0, 4.0, 5.0]]
Y = [150, 200, 250, 300, 350]  

final_w, final_b = train_linear_regression(X, Y, epochs=100, learning_rate=0.05)
print(f"\nTraining Complete! Final Line: Price = {final_w:.2f}*(SqFt) + {final_b:.2f}")
