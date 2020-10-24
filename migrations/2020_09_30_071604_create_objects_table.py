from orator.migrations import Migration


class CreateObjectsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('objects') as table:
            table.increments('appid')
            table.string('name', 512)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('objects')
