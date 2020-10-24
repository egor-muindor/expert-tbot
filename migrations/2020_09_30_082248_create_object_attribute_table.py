from orator.migrations import Migration


class CreateObjectAttributeTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('object_attribute') as table:
            table.integer('appid').unsigned()
            table.integer('attribute_id').unsigned()
            table.foreign('appid').references('appid').on('objects')
            table.foreign('attribute_id').references('id').on('attributes')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('object_attribute')
