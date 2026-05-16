import math

def calculate_log_loss(y_true, y_pred):
    y_pred = max(1e-15, min(1 - 1e-15, y_pred))
    if y_true==1:
        loss = -math.log(y_pred)
    else:
        loss = -math.log(1-y_pred)
    # loss = - y_true * math.log(y_pred) - (1- y_true) * math.log(1-y_pred)
    return loss

def activation(z):
    return 1 / (1 + math.exp(-z))

def train(X, Y, epochs=100, lr=0.01):
    w = 0.0
    b = 0.0
    n = len(X)

    for epoch in range(epochs):
        dw = 0
        db = 0
        loss = 0

        for i in range(n):
            z = w * X[i] + b
            y_hat = activation(z)

            loss += calculate_log_loss(Y[i], y_hat)

            error = y_hat - Y[i]
            dw += error * X[i]
            db += error

        w -= lr * (dw / n)
        b -= lr * (db / n)

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss/n:.4f}")

    return w, b

# --- Let's run it on some dummy housing data! ---
# features = square footage (scaled down), targets = price
X = [[1.0, 2.0, 3.0, 4.0, 5.0],
     [1.0, 2.0, 3.0, 4.0, 5.0]]
Y = [0, 1, 0, 1, 1]

final_w, final_b = train(X, Y, epochs=100, learning_rate=0.05)
print(f"\nTraining Complete! Final Line: Price = {final_w:.2f}*(SqFt) + {final_b:.2f}")
