package Dto;

import lombok.Data;

import java.sql.Timestamp;

@Data
public class Transaction {

    private String transactionId;
    private String producerId;
    private String productName;
    private String productCategory;
    private double productPrice;
    private int productQuantity;
    private String productBrand;
    private String currency;
    private String customerId;
    private Timestamp transactionDate;
    private String paymentMethod;
    private double totalAmount;

    public String getTransactionId() {
        return transactionId;
    }

    public String getProductId() {
        return producerId;
    }

    public String getProductName() {
        return productName;
    }

    public String getProductCategory() {
        return productCategory;
    }

    public double getProductPrice() {
        return productPrice;
    }

    public int getProductQuantity() {
        return productQuantity;
    }

    public String getProductBrand() {
        return productBrand;
    }

    public String getCurrency() {
        return currency;
    }

    public String getCustomerId() {
        return customerId;
    }

    public Timestamp getTransactionDate() {
        return transactionDate;
    }

    public String getPaymentMethod() {
        return paymentMethod;
    }

    public double getTotalAmount() {
        return totalAmount;
    }

}