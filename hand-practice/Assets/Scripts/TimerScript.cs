using UnityEngine;
using TMPro;

public class TimerScript : MonoBehaviour
{
    public float timeRemaining;
    public bool isRunning;

    [SerializeField] float initTime; 
    [SerializeField] TextMeshProUGUI timerCount; 

    void Start()
    {
        timeRemaining = initTime;
        timerCount.text = Mathf.RoundToInt(timeRemaining).ToString();
    }

    void Update()
    {
        if (!isRunning) return;

        timeRemaining -= Time.deltaTime;

        if(timeRemaining <= 0)
        {
            timeRemaining = 0;
            isRunning = false;
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
        isRunning = true;
    }
}
