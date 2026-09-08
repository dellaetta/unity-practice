using UnityEngine;
using TMPro;

public class TimerScript : MonoBehaviour
{
    public float timeRemaining;
    public bool isRunning;
    public float initTime = 5; 

    [SerializeField] TextMeshProUGUI timerCount; 
    [SerializeField] GameManager gameManager;

    void Update()
    {
        if (!isRunning) return;

        timeRemaining -= Time.deltaTime;

        if(timeRemaining <= 0)
        {
            timeRemaining = 0;
            isRunning = false;
            gameManager.GameOver();
        }

        timerCount.text = timeRemaining.ToString("F2");
    }

    public void StartTimer()
    {
        isRunning = true;
    }

    public void StopTimer()
    {
        isRunning = false;
    }

    public void ResetTimer()
    {
        timeRemaining = initTime;
        timerCount.text = timerCount.text = timeRemaining.ToString("F2");
        isRunning = true;
    }

    public void ReduceTime()
    {
        if(initTime >= 3)
        {
            initTime -= 0.5f;
        }
    }
}
