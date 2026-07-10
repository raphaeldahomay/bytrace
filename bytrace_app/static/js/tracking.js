function trackClick(event, eventType, clickedElement, targetUrl) {
    event.preventDefault();

    const previousPageUrl = window.location.href;
    const targetPageUrl = new URL(targetUrl, window.location.origin).href;

    fetch("/track-event", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            event_type: eventType,
            clicked_element: clickedElement,
            previous_page_url: previousPageUrl,
            target_page_url: targetPageUrl
        })
    })
    .finally(() => {
        window.location.href = targetPageUrl;
    });
}