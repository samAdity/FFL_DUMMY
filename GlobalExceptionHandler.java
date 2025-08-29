The Java code appears to be correct and has no syntax or runtime errors. It's a standard Spring Boot exception handler with proper imports, annotations, and structure.

package com.example.demo.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@ControllerAdvice
public class GlobalExceptionHandler {

    // Handle all unexpected exceptions
    @ExceptionHandler(Exception.class)
    public ResponseEntity<Object> handleServerError(Exception ex) {
        Map<String, Object> errorDetails = new HashMap<>();
        errorDetails.put("timestamp", LocalDateTime.now());
        errorDetails.put("status", HttpStatus.INTERNAL_SERVER_ERROR.value());
        errorDetails.put("error", "Internal Server Error");
        errorDetails.put("message", ex.getMessage());
        errorDetails.put("hint", "Contact support with this error ID for faster resolution.");
        errorDetails.put("errorId", "ERR-" + System.currentTimeMillis()); // unique error reference

        return new ResponseEntity<>(errorDetails, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}