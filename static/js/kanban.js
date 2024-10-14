et tasks = JSON.parse(localStorage.getItem('tasks')) || [];

document.addEventListener("DOMContentLoaded", function () {
    renderTasks();
});

// Function to render tasks on the board
function renderTasks() {
    const columns = ['newApp', 'in-progress', 'done'];

    columns.forEach(columnId => {
        const column = document.getElementById(columnId);
        column.querySelector('.task-container').innerHTML = '';

        tasks.forEach(task => {
            if (task.status === columnId) {
                const taskElement = createTaskElement(task.content, task.id);
                column.querySelector('.task-container').appendChild(taskElement);
            }
        });
    });
}

function createTaskElement(content, id) {
    const task = document.createElement("div");
    task.id = id;
    task.className = "task";
    task.draggable = true;
    task.innerHTML = `
        ${content}
        <span class="delete-btn" onclick="deleteTask('${id}')">❌</span>
    `;
    task.addEventListener("dragstart", drag);
    return task;
}

// Function to delete a task
function deleteTask(taskId) {
    tasks = tasks.filter(task => task.id !== taskId);
    updateLocalStorage();
    renderTasks();
}

function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text/plain", event.target.id);
}

function drop(event, columnId) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text/plain");
    const draggedElement = document.getElementById(data);
    if (draggedElement) {
        updateTaskStatus(data, columnId);
        event.target.querySelector('.task-container').appendChild(draggedElement);
    }
}

function addTask() {
    const taskTitle = document.getElementById('taskTitle').value.trim();
    const taskDescription = document.getElementById('taskDescription').value.trim();

    console.log("Adding Task:", taskTitle, taskDescription); // Debug log

    if (taskTitle && taskDescription) {
        const newTask = {
            id: "task-" + Date.now(),
            content: `${taskTitle}: ${taskDescription}`, // Custom content
            status: 'newApp' // Default status
        };
        tasks.push(newTask);
        updateLocalStorage();
        renderTasks();
        $('#taskModal').modal('hide'); // Close the modal
        document.getElementById('taskForm').reset(); // Reset the form
    } else {
        console.log("Please fill in both fields."); // Debug log
    }
}

// Function to update task status when moved to another column
function updateTaskStatus(taskId, newStatus) {
    tasks = tasks.map(task => {
        if (task.id === taskId) {
            return { ...task, status: newStatus };
        }
        return task;
    });
    updateLocalStorage();
}

// Function to update local storage with current tasks
function updateLocalStorage() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Event listener for the form submission
document.getElementById('submitApp').addEventListener('click', addTask);