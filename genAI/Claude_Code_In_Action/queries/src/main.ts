import { open } from "sqlite";
import sqlite3 from "sqlite3";

import { createSchema } from "./schema";
import { getPendingOrders } from "./queries/order_queries";
import { sendSlackMessage } from "./slack";

async function main() {
  const db = await open({
    filename: "ecommerce.db",
    driver: sqlite3.Database,
  });

  await createSchema(db);

  const pendingOrders = await getPendingOrders(db);
  const staleOrders = pendingOrders.filter((o) => o.days_since_created > 3);

  for (const order of staleOrders) {
    const text =
      `*Stale Pending Order Alert*\n` +
      `Order ID: ${order.order_id} has been pending for ${Math.floor(order.days_since_created)} days.\n` +
      `Customer: ${order.customer_name} | Phone: ${order.phone ?? "N/A"}`;

    await sendSlackMessage({ channel: "#order-alerts", text });
  }
}

main();
