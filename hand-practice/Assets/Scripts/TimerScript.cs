using UnityEngine;
using TMPro;

public class TimerScript : MonoBehaviour
{
    public float timeRemaining;
    public bool isRunning;

    [SerializeField] float initTime; 
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

        timerCount.text = Mathf.RoundToInt(timeRemaining).ToString();
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
        timerCount.text = Mathf.RoundToInt(timeRemaining).ToString();
        isRunning = true;
    }
}
