#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"

static const char *TAG = "SKETCH_IDF";

void app_main(void)
{
    while (1) {
        ESP_LOGI(TAG, "Prueba de compilacion ESP-IDF para ESP32");
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
