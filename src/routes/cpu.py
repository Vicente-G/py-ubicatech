from flask import Blueprint, current_app, jsonify, request

from src.database import db_exec
from src.models.cpu import (
    CPU,
    create_cpu,
    delete_cpu,
    get_all_cpus,
    get_cpu_by_id,
    update_cpu,
)

cpu_bp = Blueprint("cpu", __name__)


@cpu_bp.route("/cpus", methods=["GET"])
def get_cpus():
    current_app.logger.info("HTTP/GET: Getting all CPUs")
    cpus = db_exec(get_all_cpus)
    current_app.logger.info(f"HTTP/GET: {len(cpus)} CPUs sent")
    return jsonify(list(map(dict, cpus))), 200


@cpu_bp.route("/cpus/<int:cpu_id>", methods=["GET"])
def get_cpu(cpu_id):
    current_app.logger.info(f"HTTP/GET: Getting CPU with ID {cpu_id}")
    cpu = db_exec(get_cpu_by_id, cpu_id)
    if cpu:
        current_app.logger.info(f"HTTP/GET: CPU with ID {cpu_id} found")
        return jsonify(dict(cpu)), 200
    current_app.logger.warning(f"HTTP/GET: CPU with ID {cpu_id} not found")
    return jsonify({"error": "CPU not found"}), 404


@cpu_bp.route("/cpus", methods=["POST"])
def create_new_cpu():
    current_app.logger.info("HTTP/POST: Creating a new CPU")
    data = request.get_json()
    if not data:
        current_app.logger.warning("HTTP/POST: Invalid input for creating CPU")
        return jsonify({"error": "Invalid input"}), 400
    cpu_id = db_exec(create_cpu, CPU(**dict(data)))
    current_app.logger.info(f"HTTP/POST: CPU created with ID {cpu_id}")
    return jsonify({"message": "CPU created", "cpu_id": cpu_id}), 201


@cpu_bp.route("/cpus/<int:cpu_id>", methods=["PUT"])
def update_existing_cpu(cpu_id):
    current_app.logger.info(f"HTTP/PUT: Updating CPU with ID {cpu_id}")
    data = request.get_json()
    if not data:
        current_app.logger.warning(f"HTTP/PUT: Invalid input for updating CPU with ID {cpu_id}")
        return jsonify({"error": "Invalid input"}), 400
    updated = db_exec(update_cpu, cpu_id, data)
    if updated:
        current_app.logger.info(f"HTTP/PUT: CPU with ID {cpu_id} updated successfully")
        return jsonify({"message": "CPU updated"}), 200
    current_app.logger.warning(f"HTTP/PUT: CPU with ID {cpu_id} not found")
    return jsonify({"error": "CPU not found"}), 404


@cpu_bp.route("/cpus/<int:cpu_id>", methods=["DELETE"])
def delete_existing_cpu(cpu_id):
    current_app.logger.info(f"HTTP/DELETE: Deleting CPU with ID {cpu_id}")
    deleted = db_exec(delete_cpu, cpu_id)
    if deleted:
        current_app.logger.info(f"HTTP/DELETE: CPU with ID {cpu_id} deleted successfully")
        return jsonify({"message": "CPU deleted"}), 200
    current_app.logger.warning(f"HTTP/DELETE: CPU with ID {cpu_id} not found")
    return jsonify({"error": "CPU not found"}), 404
